package PagesTests;

import dev.failsafe.internal.util.Assert;
import org.junit.jupiter.api.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.ui.Select;

public class Address {
    @Test
    public void Adress(WebDriver driver) throws InterruptedException {
        WebElement streetname=driver.findElement(By.id("streetname"));
        streetname.clear();
        streetname.sendKeys("rozovsky");
        WebElement streetnumber=driver.findElement(By.id("streetnumber"));
        streetnumber.sendKeys("1");
        WebElement city=driver.findElement(By.id("city"));
        city.sendKeys("petach tikva");
        WebElement country=driver.findElement(By.id("country"));
        Select select=new Select(country);
        select.selectByIndex(2);
        WebElement finish= driver.findElement(By.id("finish"));
        finish.click();
        WebElement adress= driver.findElement(By.id("streetname"));
        System.out.println(adress.getText());
        if(adress.getText().equals("rozovsky"))
            Assert.isTrue(false,"street was not correct!!!!");
        isOpen(driver);
//        NewPage n=new NewPage();
//        n.newPage(driver);

    }
    public void negetiveAdress(WebDriver driver) throws InterruptedException {
        WebElement streetname=driver.findElement(By.id("streetname"));
        streetname.clear();
        streetname.sendKeys("rozovsky");
        WebElement streetnumber=driver.findElement(By.id("streetnumber"));
        streetnumber.sendKeys("1");
        WebElement city=driver.findElement(By.id("city"));
        city.sendKeys("petach tikva");
        WebElement country=driver.findElement(By.id("country"));
        Select select=new Select(country);
        select.selectByIndex(2);
        Thread.sleep(1000);
        WebElement finish= driver.findElement(By.id("finish"));
        finish.click();
        WebElement adress= driver.findElement(By.id("streetname"));
        if(adress.getText().equals("rozosky"))
            Assert.isTrue(true,"street was not correct!!!!");

    }

    @Test
    public void isOpen(WebDriver driver)throws InterruptedException {
       if( !driver.getCurrentUrl().equals("https://automation.co.il/tutorials/selenium/demo1/indexID.html"))
           Assert.isTrue(false,"the page is not found!");
        NewPage n=new NewPage();
        n.newPage(driver);

    }
}
