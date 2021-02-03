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
        [InlineData("ABAB", 2, 4)]
        [InlineData("AABABBA", 1, 4)]
        public void Run_TestCaseType1(string s, int k, int expectedResult)
        {
            var actualResult = _mainService.Run(s, k);
            Assert.Equal(expectedResult, actualResult);
        }
    }
}

/**
 * To run in Visual Studio, press `Ctrl+R, A`
 * In VS Code, type `dotnet test`
 * 
 */
