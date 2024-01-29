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
        [InlineData("abcabcbb", 3)]
        [InlineData("bbbbb", 1)]
        [InlineData("pwwkew", 3)]
        [InlineData("", 0)]
        [InlineData("xxzpi", 4)]
        public void Run_TestCaseType1(string s, int expectedResult)
        {
            var actualResult = _mainService.Run(s);
            Assert.Equal(expectedResult, actualResult);
        }
    }
}

/**
 * To run in Visual Studio, press `Ctrl+R, A`
 * In VS Code, type `dotnet test`
 * 
 */
