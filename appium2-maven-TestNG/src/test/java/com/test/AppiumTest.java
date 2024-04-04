package com.test;

import io.appium.java_client.android.AndroidDriver;
import io.appium.java_client.android.options.UiAutomator2Options;
import io.appium.java_client.remote.AutomationName;
import org.junit.Test;

import java.net.MalformedURLException;
import java.net.URL;

public class AppiumTest {

    @Test
    public void launchAndroidTest() throws MalformedURLException {
        UiAutomator2Options options = new UiAutomator2Options();
        options.setPlatformName("Android");
        options.setAutomationName(AutomationName.ANDROID_UIAUTOMATOR2);
        options.setDeviceName("Local-Android-Device");
        options.setApp(System.getProperty("user.dir") + "/apps/test-app-android.apk");

        AndroidDriver driver = new AndroidDriver(
            new URL("http://0.0.0.0:4723"),
            options
        );
    }
}
