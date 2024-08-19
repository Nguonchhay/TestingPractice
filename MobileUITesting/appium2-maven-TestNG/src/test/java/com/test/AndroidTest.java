package com.test;

import io.appium.java_client.android.AndroidDriver;
import io.appium.java_client.android.options.UiAutomator2Options;
import io.appium.java_client.remote.AutomationName;
import org.junit.Test;

import java.io.IOException;
import java.net.MalformedURLException;
import java.net.URL;

public class AndroidTest extends AppiumTest {
    protected UiAutomator2Options options;

    public AndroidTest() throws IOException {
        super();
        testDeviceName = "Local-Android-Device";

        options = new UiAutomator2Options();
        options.setPlatformName("Android");
        options.setAutomationName(AutomationName.ANDROID_UIAUTOMATOR2);
        options.setDeviceName("Local-Android-Device");
        options.setApp(getTestAppPath("test-app-android.apk"));
    }

    @Test
    public void launchTest() throws MalformedURLException {
        AndroidDriver driver = new AndroidDriver(
                new URL(super.appiumServerUrl),
                options
        );
    }
}
