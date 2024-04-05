package com.test;

import configs.Property;

public class AppiumTest {

    protected String appiumServerUrl;

    protected Property property;
    protected String testDeviceName;

    public AppiumTest() {
        property = Property.getInstance();
        appiumServerUrl = property.getConfigValue("HOST");
        testDeviceName = "Testing Device";
    }

    public String getTestAppPath(String filename) {
        return property.getProjectPath() + "apps/" + filename;
    }
}
