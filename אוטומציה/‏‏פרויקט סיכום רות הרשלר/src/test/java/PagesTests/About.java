package PagesTests;

import org.junit.jupiter.api.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.time.Duration;

public class About {
    @Test
    public void About() throws InterruptedException {
        WebDriver driver = new ChromeDriver();
        WebDriverWait wait=new WebDriverWait(driver, Duration.ofSeconds(5));
        driver.get(" https://automation.co.il/tutorials/selenium/demo1/indexID.html");
        driver.manage().window().fullscreen();
        Thread.sleep(1000);
        WebElement firstname=driver.findElement(By.id("firstname"));
        firstname.sendKeys("ruth");
        WebElement lastname=driver.findElement(By.id("lastname"));
        lastname.sendKeys("hershler");
        WebElement email=driver.findElement(By.id("email"));
        email.sendKeys("ruth0533137873@gmail.com");
        Thread.sleep(1000);
        WebElement next= driver.findElement(By.id("next"));
        next.click();
        Account ac=new Account();
        ac.Account(driver);
        Thread.sleep(1000);

        driver.close();
    }
}
