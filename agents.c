/**********************************************************************************************
 File: agents.c

**********************************************************************************************/

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <time.h>
#include <errno.h>
#include <pthread.h>
#include <stdatomic.h>
#include <semaphore.h>
#include "agents.h"
/****************************************/                                      
int init (int);
int check_point(int*);
void go_agent (char *);
int log_sum (char *);
int update(int, char *, char * );
int write_to_log(int, char *);
void fatal_error(char *,char *);
int gen_rand(int);
void controller_thread(int*);
/**********************************************************************/
/*           Global Array - All Agents' names              */
char agents[ MAX_AGENTS ][ NAMES_LEN ] = AGENTS;
int p ; /* number of the started agentes */ 
pthread_t thread[MAX_AGENTS]/*agents*/, cThread/*control thtead*/;
sem_t mutex_agents;
sem_t mutex_controller;
/**********************************************************************/

/* Reset all files,Dispatch all agents and control actions */
int main(int ac,char **av ) 
{
  int i = 0, num_agents = 1;/* default */  
  if ( ac == 2 )  i = atoi( av[1] );  /* Check arguments */ 
  else if (ac != 1) fatal_error("USAGE:agents [number_of_agents]\n", NULL);    
  /* initiate an account file with a start sum */
  num_agents = init( i );
  if(sem_init(&mutex_agents, 0, 1)!=0)
  	fatal_error("semaphore agents init error\n",NULL);
  if(sem_init(&mutex_controller, 0, 1)!=0)
  	fatal_error("semaphore controller init error\n",NULL);
  	 
  /* Main process distributes work to threads (agents).
     Agents perform independent operations.Every agent updates the account file
     after each operation and logs them in a personal log file */
  for(i=0, p=0 ; i < num_agents; i++, p++ ){  
  if(pthread_create(&thread[p], NULL, (void *)go_agent, &agents[p]))
    { perror("ERROR creating thread."); --p; }
    }
  i = p;
  printf("Finished creating %d agent(s). \n",num_agents);
  //sleep(1);  
  /* The father waits for agents to return succesfully */ 
 // while ( p >= 1 ) { sleep(2);} //!!!Have to transfer to check_point
/* check the consistency(log files vs.the account file. */ 
//  check_point( &i );
  
  if(pthread_create(&cThread,NULL,(void*)controller_thread,&i))
  	{ fatal_error("create controller thread failed\n",NULL);}
  	  
  pthread_join(cThread,NULL);
  //יצירת טרד
  //המתנה לטרד
  sem_destroy(&mutex_agents); 
  sem_destroy(&mutex_controller); 

  return 0;
}
			
/********************************************************************/
/*  initiate the account file with the starting sum 
 *  return the number of agents to be created in the range [1, MAX_AGENTS] */ 
int init(int num_agents )   /* Initiate auxiliary files,returns number agents */
{
   FILE *fp;
   int i;
   //srand( time( NULL ) ); // seeds rand()
   if ( num_agents < 1 || num_agents > MAX_AGENTS ){
     printf("%d agent(s) defaults to 1\n",num_agents);
     num_agents = 1;
    }
   printf("Creating %d agent(s). \n",num_agents);
   // delete old files; exit if fails
   for ( i = 0; i < num_agents; i++)
       if ((unlink( agents[i] ) < 0) && (errno != ENOENT)  )
          fatal_error("Deleting agents log", "");  
   if (( fp = fopen( ACCOUNT,"w")) == NULL )
        fatal_error("Creating ACCOUNT file", "");
   fprintf( fp,"%d\n",START_SUM );
   fclose( fp );
   return( num_agents );
}
/*******************************************************************/

int check_point(int * num_agents ) /* Are agents' actions consistent ? */
{
 int i, control_sum , sum ;
   control_sum=0;
   sem_wait(&mutex_controller);
   printf("\n\n ----- Controler ----- \n");
   if ((sum = update(0,ACCOUNT, NULL )) == ERROR)
   { 
//   sem_post(&mutex_controller);
   return(ERROR);//get the sum by updating 0
   } 
   for ( i = 0; i < *num_agents; ++i )
        control_sum = control_sum + log_sum( agents[i] );
   //שחרור
   sem_post(&mutex_controller); 
   control_sum = START_SUM + control_sum; 
   
   if  ( sum != control_sum )
   {
      fprintf( stderr,"\n Not consistent! Somebody steals?!\n");
      fprintf( stderr,"Controler: %d, Account: %d \n",control_sum,sum );
	  fprintf( stderr," Terminating all agents!\n");
	  return(1);
   }
   printf("\nOperations O.K. Controler: %d, Acount: %d\n", control_sum, sum ); 
}
/**********************************************************************/
int log_sum(char *log_file )    /* Returns the sum of log_file */
{
   FILE  *fp;
   int sum = 0,tmp_sum;
   if ( ( fp = fopen( log_file ,"r+") ) == NULL )
   {
      perror( log_file );
      printf("\nCan't Control %s agent!\n",log_file );
      return( 0 );
   }
   while ( fscanf( fp,"%d",&tmp_sum ) > 0 ) sum = sum + tmp_sum;
   fclose( fp ); 
   printf(" Sum of %s = %d\n",log_file,sum );
   return( sum );
}
/*****************************************************************/
void fatal_error(char *err_msg,char *perror_arg)  /* Prints Error messages */
{
  fprintf(stderr,"\nERROR: %s. ", err_msg);
  if ( perror_arg != NULL ) perror( perror_arg);
  exit(ERROR);    
}
/*************************************************************************/

void go_agent(char *agent_name)      /* sends agent to work */
{
  int n, i, amount;
    for( i = 0; i < OPERATIONS ; ++i )
	{
	  amount = gen_rand( MAX_OPER );
	//
	sem_wait(&mutex_controller);
	  if ( update( amount,ACCOUNT, agent_name ) == ERROR )
	  {
		  fatal_error( "Can't Update Account File", ACCOUNT); //It includes process termination
	  }
      else {		 
	    if ( write_to_log( amount,agent_name ) == ERROR ){ // rollback	   
	      if (update(-amount, ACCOUNT, NULL ) == ERROR)
	       fprintf(stderr, "ERROR: Rollback failed. Agent %s\n", agent_name);
	    fatal_error( "Can't log operations", agent_name); //It includes process termination
	     }
	   }
	  //שחרור הסמפור
	  sem_post(&mutex_controller);
	  printf(" Op of %s = %d\n",agent_name,amount );
	  if ( ( n = rand() % MAX_SLEEP ) != 0 )  sleep( n );
	}
	p--;
    printf(" Agent %s : Succefull!\n",agent_name ); 
   return;
}
/**************************************************************/
int gen_rand(int range)/*Generates random numbers between -rang and +range*/
{                     
   int n,sign;
   static int s=17;
   srand( time( NULL ) % s++);
   while( ( n = rand() ) == 0 );
   sign = (n/1111) % 2;
   n = ( (n/1117) % range ) + 1;
   if ( sign == 0 )  return( n );
   else return( 0 - n );
}
/*********************************************************************/
/* Updates account using amount. Returns new sum */
int update(int amount,char *account, char * name )  
{
   FILE  *fp;
   int n; 
   char buf[ BUF_LENGTH ];
   memset (buf, '\0',  BUF_LENGTH);
   //סמפור
   sem_wait(&mutex_agents);
   if ( !(fp = fopen( account , "r"))) return( ERROR );    
   fscanf (fp, "%s", buf);
   fclose( fp );
   //if ( amount != 0 )  printf("%s", "."); //uncomment to se the progress,not needed 
   if (!( fp = fopen( account,"w" )))  return( ERROR );
   fprintf( fp,"%d", n = atoi(buf) + amount );
   fclose( fp );
   sem_post(&mutex_agents);
   return( n + amount );               /* New sum in account */
}
/*******************************************************************/
int write_to_log(int amount,char *log_file )  /* Appends amount to log_file */
{
   FILE *fp;
   if ((fp = fopen( log_file,"a")) == NULL ) return( ERROR );
   fprintf( fp,"%d\n",amount );
   fclose( fp );
   return( SUCCESS );
}
/******************************************************************/
void controller_thread(int* i)  
{
int n;
	printf("controller_thread,p=%d\n",p);
	
	while(p>=1){
		printf(">>>>>>>>>>>>>>>>>>>p is %d i=%d\n",p,*i);
  		if ( ( n = rand() % MAX_SLEEP) != 0 ) sleep( n * 3 );
		check_point(i);
	}
	for(int j = 0; j < *i; j++){
   		pthread_join(thread[j],NULL);
   }
      check_point( i );
      exit(SUCCESS);
}
/***************************EOF*****************************/
