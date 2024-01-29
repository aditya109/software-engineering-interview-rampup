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
        [InlineData(new char[] { 'A', 'A', 'A', 'H', 'H', 'I', 'B', 'C' }, 2, 5)]
        public void Run_TestCaseType1(char[] arr, int k, int expectedResult)
        {
            var actualResult = _mainService.LongestSubstringLength(arr, k);
            Assert.Equal(expectedResult, actualResult);
        }
    }
}

/**
 * To run in Visual Studio, press `Ctrl+R, A`
 * In VS Code, type `dotnet test`
 * 
 */
