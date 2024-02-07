package PagesTests;

import org.junit.jupiter.api.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

public class Account {
    @Test
    public void Account(WebDriver driver) throws InterruptedException {
        WebElement Beginner=driver.findElement(By.id("Beginner"));
        Beginner.click();
        Thread.sleep(500);
        WebElement next= driver.findElement(By.id("next"));
        next.click();
Address a=new Address();
a.negetiveAdress(driver);//בדיקה שלילית
a.Adress(driver);
    }
}
