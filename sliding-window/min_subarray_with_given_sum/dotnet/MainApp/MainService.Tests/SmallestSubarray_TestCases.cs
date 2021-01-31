using Main.Service;
using Xunit;

namespace Main.UnitTests.Service
{
    public class SmallestSubarray_TestCases
    {
        private readonly MainService _mainService;

        public Run_TestCases()
        {
            _mainService = new MainService();
        }

        [Theory]
        [InlineData(8, new int[] { 4, 2, 2, 7, 8, 1, 2, 8, 10 }, 1)]
        public void SmallestSubarray_TestCaseType1(int targetSum, int[] arr, int expectedResult)
        {
            var actualResult = _mainService.SmallestSubarray(targetSum, arr);
            Assert.Equal(expectedResult, actualResult);
        }
    }
}

/**
 * To run in Visual Studio, press `Ctrl+R, A`
 * In VS Code, type `dotnet test`
 * 
 */