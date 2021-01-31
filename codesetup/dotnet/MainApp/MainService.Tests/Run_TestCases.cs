using Main.Service;
using Xunit;

namespace Main.UnitTests.Service
{
    public class Run_TestCases
    {
        private readonly MainService _mainService;

        public SmallestSubarray_TestCases()
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

/**
 * To run in Visual Studio, press `Ctrl+R, A`
 * In VS Code, type `dotnet test`
 * 
 */
