package tests;

import PagesTests.About;
import PagesTests.Account;
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
    public void ChromeStore() throws InterruptedException {
        About a=new About();
        a.About();
    }

}
