package PagesTests;

import dev.failsafe.internal.util.Assert;
import org.junit.jupiter.api.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;

public class NewPage {
    @Test
    public void newPage(WebDriver driver) throws InterruptedException {
        WebElement startAgain= driver.findElement(By.id("startAgain"));
        startAgain.click();

        WebElement firstname=driver.findElement(By.id("firstname"));
        WebElement lastname=driver.findElement(By.id("lastname"));
        WebElement email=driver.findElement(By.id("email"));
       if(! firstname.getText().equals("")||!lastname.getText().equals("")||!email.getText().equals(""))
        Assert.isTrue(false,"the page is not empty!");
    }
}
