# Steps to run example codebase in <img src="https://cdn.svgporn.com/logos/dotnet.svg" height="50"/> 

> The C# implementation of a particular problem is written such that the code can be freely tested amongst numerous test cases.

To run a particular code implementation in `.NET` for a particular problem set, navigate to the specific problem set.  

Let's say the problem set is `max_sum_of_contingous_subarray_of_size_n` under `sliding-window`.

So we navigate to `grokking-the-coding-interview` > `sliding-window` > `max_sum_of_contingous_subarray_of_size_n` > `dotnet` > `MainApp`.

For `C#`, you could either use `Visual Studio` or any text editor of your choice. I am using `VS Code` for demonstration.

## Repository Explanation

1. The directory structure visible would be something like this:

   ```powershell
   MAINAPP
   ├───MainService
   │   ├───bin
   │   ├───obj
   │   ├───Properties
   │   ├───MainService.cs
   │   └───MainService.csproj
   ├───MainService.Tests
   │   ├───bin
   │   ├───obj
   │   ├───Run_TestCases.cs
   │   └───MainService.Tests.csproj
   └───MainApp.sln
   ```

2. `MainService` \ `MainService.cs` is the program where actual code resides. The main code resides within `Run()`.

   ```c#
   namespace Main.Service
   {
       public class MainService
       {
           public void Run()
           {
   			// write your code here
           }
       }
   }
   ```

3.  `MainService.Tests` / `Run_TestCases.cs` is the program where unit tests reside.

   ```c#
   using Main.Service;
   using Xunit;
   
   namespace Main.UnitTests.Service
   {
       public class Run_TestCases
       {
           private readonly MainService _mainService;
   
           public Run_TestCases()
           {
               _mainService = new MainService();
           }
   
           [Theory]
           [InlineData()]
           public void Run_TestCaseType1()
           {
           }
       }
   }
   ```

## Steps for `VS Code` users:

1. Open the `MainApp` in `VS Code`.

2. Open `Powershell Terminal`.

   ```powershell
   🐳 :: MainApp » dotnet test
   Determining projects to restore...
   All projects are up-to-date for restore.
   MainService -> D:\Work\go-workspace\src\github.com\aditya109\grokking-the-coding-interview\codesetup\dotnet\MainApp\MainService\bin\Debug\MainService.dll
   MainService.Tests -> D:\Work\go-workspace\src\github.com\aditya109\grokking-the-coding-interview\codesetup\dotnet\MainApp\MainService.Tests\bin\Debug\netcoreapp3.1\MainService.Tests.dll
   Test run for D:\Work\go-workspace\src\github.com\aditya109\grokking-the-coding-interview\codesetup\dotnet\MainApp\MainService.Tests\bin\Debug\netcoreapp3.1\MainService.Tests.dll (.NETCoreApp,Version=v3.1)
   Microsoft (R) Test Execution Command Line Tool Version 16.8.3
   Copyright (c) Microsoft Corporation.  All rights reserved.
   
   Starting test execution, please wait...
   A total of 1 test files matched the specified pattern.
   
   Passed!  - Failed:     0, Passed:     1, Skipped:     0, Total:     1, Duration: 1 ms - MainService.Tests.dll (netcoreapp3.1)
   ```

## Steps for `Visual Studio` users:

1. Open the `MainApp.sln` using `Visual Studio`.

2. Open `Solution Explorer` and right-click on `MainService.Tests` and `Run Tests`.

