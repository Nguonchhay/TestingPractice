package configs;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;
import io.github.cdimascio.dotenv.Dotenv;

public class Property {

    static Property instance;

    private Property() {}

    public static Property getInstance() {
        if (instance == null) {
            instance = new Property();
        }
        return instance;
    }

    public String getConfigValue(String key) {
        Dotenv dotenv = Dotenv.configure().load();
        return dotenv.get(key);
    }

    public String readFile(String pathAndFileName) {
        try {
            File file = new File(pathAndFileName);
            Scanner sc = new Scanner(file);
            // We just need to use \\Z as delimiter
            sc.useDelimiter("\\Z");
            return sc.next();
        } catch (IOException e) {
            e.printStackTrace();
            return "";
        }
    }

    public void writeFile(String pathAndFileName, String content) {
        try {
            FileWriter writer = new FileWriter(pathAndFileName, false);
            writer.write(content);
            writer.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    /**
     * @return String
     */
    public String getProjectPath() {
        return System.getProperty("user.dir") + "/";
    }
}
