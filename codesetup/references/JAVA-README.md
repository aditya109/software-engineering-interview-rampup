# Steps to run example codebase in <img src="https://cdn.svgporn.com/logos/java.svg" height="50"/> 

> The Java implementation of a particular problem is written such that the code can be freely tested amongst numerous test cases.

To run a particular code implementation in `golang` for a particular problem set, navigate to the specific problem set.  

Let's say the problem set is `max_sum_of_contingous_subarray_of_size_n` under `sliding-window`.

So we navigate to `grokking-the-coding-interview` > `sliding-window` > `max_sum_of_contingous_subarray_of_size_n` > `java` > `MainApp`.

For `java`, you could either use any text editor of your choice. I am using `VS Code` for demonstration.

## Repository Explanation

1. The directory structure visible would be something like this:

   ```powershell
   MAINAPP
   └───src
       ├───main
       │   ├───java
       │   │   └───io
       │   │       └───github
       │   │           └───mainapp
       │   │               └───MainApp.java
       │   └───resources
       └───test
           └───java
               └───io
                   └───github
                       └───mainapp
                       	├───MainAppTest.java
                       	└───TestArgumentsProvider.java
   ```

2. `MainApp.java` is the program where actual code resides. The main code resides within `Run()`.

   ```java
   package io.github.mainapp;
   
   public class MainApp {
       public int Run(int [] arr, int k) {
           return k;
       }
   }
   ```

3. `MainAppTest.java` is the program where unit tests driver reside.

   ```java
   package io.github.mainapp;
   
   import org.junit.jupiter.api.BeforeEach;
   import org.junit.jupiter.params.ParameterizedTest;
   import org.junit.jupiter.params.provider.ArgumentsSource;
   
   import static org.junit.jupiter.api.Assertions.assertEquals;
   
   public class MainAppTest {
       private MainApp mainApp;
   
       @BeforeEach
       public void setUp() throws Exception {
           mainApp = new MainApp();
       }
   
       @ParameterizedTest
       @ArgumentsSource(TestArgumentsProvider.class)
       public void testMainAppWithTestCases(int[] arr, int k, int expectedResult) {
           int actualResult = mainApp.Run(arr, expectedResult);
           assertEquals(expectedResult, actualResult, "Wrong answer");
       }
   }
   ```

4. `TestArgumentsProvider.java` is the program where unit test cases reside.

   ```java
   package io.github.mainapp;
   
   import org.junit.jupiter.api.extension.ExtensionContext;
   import org.junit.jupiter.params.provider.Arguments;
   import org.junit.jupiter.params.provider.ArgumentsProvider;
   
   import java.util.stream.Stream;
   
   public class TestArgumentsProvider implements ArgumentsProvider {
       @Override
       public Stream<? extends Arguments> provideArguments(ExtensionContext context) {
           return Stream.of(
                   Arguments.of(new int[]{3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4}, 2, 5),
                   Arguments.of(new int[]{3, 3, 3, 1, 1, 2, 3, 3, 4}, 2, 5)
           );
       }
   }
   ```

## Steps for `VS Code` users:

1. Open the `MainApp` in `VS Code`.

2. Open `Powershell Terminal`.

   ```powershell
   🐳 :: MainApp » mvn test
   [INFO] Scanning for projects...
   [INFO]
   [INFO] -------------------------< github.io:MainApp >--------------------------
   [INFO] Building MainApp 1.0-SNAPSHOT
   [INFO] --------------------------------[ jar ]---------------------------------
   [INFO]
   [INFO] --- maven-resources-plugin:2.6:resources (default-resources) @ MainApp ---
   [WARNING] Using platform encoding (Cp1252 actually) to copy filtered resources, i.e. build is platform dependent!
   [INFO] Copying 0 resource
   [INFO]
   [INFO] --- maven-compiler-plugin:3.1:compile (default-compile) @ MainApp ---
   [INFO] Changes detected - recompiling the module!
   [WARNING] File encoding has not been set, using platform encoding Cp1252, i.e. build is platform dependent!
   [INFO] Compiling 1 source file to D:\Work\go-workspace\src\github.com\aditya109\grokking-the-coding-interview\codesetup\java\MainApp\target\classes
   [INFO]
   [INFO] --- maven-resources-plugin:2.6:testResources (default-testResources) @ MainApp ---
   [WARNING] Using platform encoding (Cp1252 actually) to copy filtered resources, i.e. build is platform dependent!
   [INFO] skip non existing resourceDirectory D:\Work\go-workspace\src\github.com\aditya109\grokking-the-coding-interview\codesetup\java\MainApp\src\test\resources
   [INFO]
   [INFO] --- maven-compiler-plugin:3.1:testCompile (default-testCompile) @ MainApp ---
   [INFO] Changes detected - recompiling the module!
   [WARNING] File encoding has not been set, using platform encoding Cp1252, i.e. build is platform dependent!
   [INFO] Compiling 2 source files to D:\Work\go-workspace\src\github.com\aditya109\grokking-the-coding-interview\codesetup\java\MainApp\target\test-classes
   [INFO]
   [INFO] --- maven-surefire-plugin:2.22.2:test (default-test) @ MainApp ---
   Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire-junit-platform/2.22.2/surefire-junit-platform-2.22.2.pom
   Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire-junit-platform/2.22.2/surefire-junit-platform-2.22.2.pom (7.0 kB at 4.9 kB/s)
   Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire-providers/2.22.2/surefire-providers-2.22.2.pom
   Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire-providers/2.22.2/surefire-providers-2.22.2.pom (2.5 kB at 6.3 kB/s)
   Downloading from central: https://repo.maven.apache.org/maven2/org/junit/platform/junit-platform-launcher/1.3.1/junit-platform-launcher-1.3.1.pom
   Downloaded from central: https://repo.maven.apache.org/maven2/org/junit/platform/junit-platform-launcher/1.3.1/junit-platform-launcher-1.3.1.pom (2.2 kB at 5.6 kB/s)
   Downloading from central: https://repo.maven.apache.org/maven2/org/apiguardian/apiguardian-api/1.0.0/apiguardian-api-1.0.0.pom
   Downloaded from central: https://repo.maven.apache.org/maven2/org/apiguardian/apiguardian-api/1.0.0/apiguardian-api-1.0.0.pom (1.2 kB at 2.9 kB/s)
   Downloading from central: https://repo.maven.apache.org/maven2/org/junit/platform/junit-platform-engine/1.3.1/junit-platform-engine-1.3.1.pom
   Downloaded from central: https://repo.maven.apache.org/maven2/org/junit/platform/junit-platform-engineDownloading from central: https://repo.maven.apache.org/maven2/org/junit/platform/junit-platform-commons/1.3.1/junit-platform-commons-1.3.1.pom
   Downloaded from central: https://repo.maven.apache.org/maven2/org/junit/platform/junit-platform-commons/1.3.1/junit-platform-commons-1.3.1.pom (2.0 kB at 5.0 kB/s)
   Downloading from central: https://repo.maven.apache.org/maven2/org/opentest4j/opentest4j/1.1.1/opentest4j-1.1.1.pom
   Downloaded from central: https://repo.maven.apache.org/maven2/org/opentest4j/opentest4j/1.1.1/opentest4j-1.1.1.pom (1.7 kB at 4.3 kB/s)
   Downloading from central: https://repo.maven.apache.org/maven2/org/apiguardian/apiguardian-api/1.0.0/apiguardian-api-1.0.0.jar
   Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire-junit-platform/2.22.2/surefire-junit-platform-2.22.2.jar
   Downloading from central: https://repo.maven.apache.org/maven2/org/junit/platform/junit-platform-engine/1.3.1/junit-platform-engine-1.3.1.jar
   Downloading from central: https://repo.maven.apache.org/maven2/org/junit/platform/junit-platform-launcher/1.3.1/junit-platform-launcher-1.3.1.jar
   Downloading from central: https://repo.maven.apache.org/maven2/org/junit/platform/junit-platform-commons/1.3.1/junit-platform-commons-1.3.1.jar
   Downloaded from central: https://repo.maven.apache.org/maven2/org/apiguardian/apiguardian-api/1.0.0/apiguardian-api-1.0.0.jar (2.2 kB at 5.5 kB/s)
   Downloading from central: https://repo.maven.apache.org/maven2/org/opentest4j/opentest4j/1.1.1/opentest4j-1.1.1.jar
   Downloaded from central: https://repo.maven.apache.org/maven2/org/opentest4j/opentest4j/1.1.1/opentest4j-1.1.1.jar (7.1 kB at 18 kB/s)
   Downloaded from central: https://repo.maven.apache.org/maven2/org/junit/platform/junit-platform-launcher/1.3.1/junit-platform-launcher-1.3.1.jar (95 kB at 90 kB/s)
   Downloaded from central: https://repo.maven.apache.org/maven2/org/junit/platform/junit-platform-commons/1.3.1/junit-platform-commons-1.3.1.jar (78 kB at 73 kB/s)
   Downloaded from central: https://repo.maven.apache.org/maven2/org/junit/platform/junit-platform-engine/1.3.1/junit-platform-engine-1.3.1.jar (135 kB at 120 kB/s)
   Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire-junit-platform/2.22.2/surefire-junit-platform-2.22.2.jar (66 kB at 44 kB/s)
   [INFO]
   [INFO] -------------------------------------------------------
   [INFO]  T E S T S
   [INFO] -------------------------------------------------------
   [INFO] Running io.github.mainapp.MainAppTest
   [INFO] Tests run: 2, Failures: 0, Errors: 0, Skipped: 0, Time elapsed: 0.067 s - in io.github.mainapp.MainAppTest
   [INFO]
   [INFO] Results:
   [INFO]
   [INFO] Tests run: 2, Failures: 0, Errors: 0, Skipped: 0
   [INFO]
   [INFO] ------------------------------------------------------------------------
   [INFO] BUILD SUCCESS
   [INFO] ------------------------------------------------------------------------
   [INFO] Total time:  9.024 s
   [INFO] Finished at: 2021-02-07T14:58:14+05:30
   [INFO] ------------------------------------------------------------------------
   ```

