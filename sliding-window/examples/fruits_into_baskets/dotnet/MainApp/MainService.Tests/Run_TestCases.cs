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
        [InlineData(new int[] { 1, 2, 1 }, 2, 3)]
        [InlineData(new int[] { 0, 1, 2, 2 }, 2, 3)]
        [InlineData(new int[] { 1, 2, 3, 2, 2 }, 2, 4)]
        [InlineData(new int[] { 3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4 }, 2, 5)]
        public void Run_TestCaseType1(int[] tree, int basketCount, int expectedResult)
        {
            var actualResult = _mainService.Run(tree, basketCount);
            Assert.Equal(expectedResult, actualResult);
        }
    }
}

/**
 * To run in Visual Studio, press `Ctrl+R, A`
 * In VS Code, type `dotnet test`
 * 
 */
