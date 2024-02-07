package tests;

import dev.failsafe.internal.util.Assert;
import org.junit.jupiter.api.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.edge.EdgeDriver;
import org.openqa.selenium.support.ui.Select;

public class ChromeTest {
    @Test
    public void ChromeTest() throws InterruptedException {
        WebDriver driver = new ChromeDriver();
        driver.get("https://www.google.com/");
        driver.manage().window().fullscreen();
        Thread.sleep(1000);
        driver.manage().window().minimize();
        driver.quit();
        driver.close();
    }

    @Test
    public void EgeTest() throws InterruptedException {
        WebDriver driver = new EdgeDriver();
        driver.get("https://www.google.com/");
        driver.manage().window().fullscreen();
        Thread.sleep(1000);
        driver.manage().window().minimize();
        driver.quit();
        //driver.close();
    }

    @Test
    public void ChromeStore() throws InterruptedException {
        WebDriver driver = new ChromeDriver();
        driver.get("https://demo.guru99.com/payment-gateway/index.php");
        driver.manage().window().fullscreen();
        Thread.sleep(1000);
        //select element
        WebElement selectq=driver.findElement(By.name("quantity"));
        Select selectQuantity=new Select(selectq);
        selectQuantity.selectByIndex(4);

        WebElement inputBuy= driver.findElement(By.tagName("input"));
        inputBuy.click();
        WebElement h2= driver.findElement(By.tagName("h2"));
        String str=h2.getText();
        if(str.equalsIgnoreCase("Payment Process"))
            driver.manage().window().fullscreen();
        else
                    Assert.isTrue(false,"expalin the failure");
         //card number
        WebElement cardNum=driver.findElement(By.id("card_nmuber"));
        cardNum.sendKeys("1234123412341234");

        //month
        WebElement eMonth=driver.findElement(By.id("month"));
        Select selectMonth=new Select(eMonth);
        selectMonth.selectByIndex(12);
        //year
        WebElement eYear=driver.findElement(By.id("year"));
        Select selectYear=new Select(eYear);
        selectYear.selectByVisibleText("2024");

        //cvv
        WebElement eCVV=driver.findElement(By.id("cvv_code"));
        eCVV.sendKeys("123");
        //click pay
        WebElement inputPay= driver.findElement(By.name("submit"));
        inputPay.click();
        h2= driver.findElement(By.tagName("h2"));
        str=h2.getText();
        if(str.equalsIgnoreCase("Payment successfull!"))
            driver.manage().window().fullscreen();
        else
            Assert.isTrue(false,"you didnt come to the current page");
        driver.quit();
        driver.quit();
    }
    @Test
    public void EdgeStore() throws InterruptedException {
        WebDriver driver = new EdgeDriver();
        driver.get("https://demo.guru99.com/payment-gateway/index.php");
        driver.manage().window().fullscreen();
        Thread.sleep(1000);
        //select element
        WebElement selectq=driver.findElement(By.name("quantity"));
        Select selectQuantity=new Select(selectq);
        selectQuantity.selectByIndex(4);

        WebElement inputBuy= driver.findElement(By.tagName("input"));
        inputBuy.click();
        WebElement h2= driver.findElement(By.tagName("h2"));
        String str=h2.getText();
        if(str.equalsIgnoreCase("Paymentrocess"))
            driver.manage().window().fullscreen();
        else
            Assert.isTrue(false,"expalin the failure");
        //card number
        WebElement cardNum=driver.findElement(By.id("card_nmuber"));
        cardNum.sendKeys("1234123412341234");

        //month
        WebElement eMonth=driver.findElement(By.id("month"));
        Select selectMonth=new Select(eMonth);
        selectMonth.deselectByVisibleText("12");
        //year
        WebElement eYear=driver.findElement(By.id("year"));
        Select selectYear=new Select(eYear);
        selectYear.deselectByVisibleText("2024");

        //cvv
        WebElement eCVV=driver.findElement(By.id("cvv_code"));
        eCVV.sendKeys("123");
        //click pay
        WebElement inputPay= driver.findElement(By.name("submit"));
        inputBuy.click();

        h2= driver.findElement(By.tagName("h2"));
        str=h2.getText();
        if(str.equalsIgnoreCase("Payment successfull!"))
            driver.manage().window().fullscreen();
        else
            Assert.isTrue(false,"you didnt come to the current page");
        driver.quit();

    }
    @Test
    public void CreditCardTest() throws InterruptedException {
        WebDriver driver = new EdgeDriver();
        driver.get("https://demo.guru99.com/payment-gateway/index.php");
        driver.manage().window().fullscreen();
        Thread.sleep(1000);
        //select element
        WebElement selectq=driver.findElement(By.name("quantity"));
        Select selectQuantity=new Select(selectq);
        selectQuantity.selectByIndex(4);

        WebElement inputBuy= driver.findElement(By.tagName("input"));
        inputBuy.click();
        WebElement h2= driver.findElement(By.tagName("h2"));
        String str=h2.getText();
        if(str.equalsIgnoreCase("Paymentrocess"))
            driver.manage().window().fullscreen();
        else
            Assert.isTrue(false,"expalin the failure");
        //card number
        WebElement cardNum=driver.findElement(By.id("card_nmuber"));
        cardNum.sendKeys("12341234123");


        //month
        WebElement eMonth=driver.findElement(By.id("month"));
        Select selectMonth=new Select(eMonth);
        selectMonth.deselectByVisibleText("12");
        //year
        WebElement eYear=driver.findElement(By.id("year"));
        Select selectYear=new Select(eYear);
        selectYear.deselectByVisibleText("2024");

        //cvv
        WebElement eCVV=driver.findElement(By.id("cvv_code"));
        eCVV.sendKeys("123");
        //click pay
        WebElement inputPay= driver.findElement(By.name("submit"));
        inputBuy.click();

        h2= driver.findElement(By.tagName("h2"));
        str=h2.getText();
        if(str.equalsIgnoreCase("Payment successfull!"))
            driver.manage().window().fullscreen();
        else
            Assert.isTrue(false,"you didnt come to the current page");
        driver.quit();
    }
    

}
