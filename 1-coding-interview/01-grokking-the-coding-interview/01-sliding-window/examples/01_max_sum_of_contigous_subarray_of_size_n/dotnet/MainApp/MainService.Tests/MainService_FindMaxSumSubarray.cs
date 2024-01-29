using Main.Service;
using Xunit;

namespace Main.UnitTests.Services
{
    public class MainService_FindMaxSumSubarray
    {
        private readonly MainService _mainService;
        public MainService_FindMaxSumSubarray()
        {
            _mainService = new MainService();
        }

        [Theory]
        [InlineData(new int[] { 4, 2, 1, 7, 8, 1, 2, 8, 1, 0 }, 3, 16)]
        [InlineData(new int[] { 4, 2, 1, 7, 8, 1, 2, 8, 1, 0 }, 4, 19)]
        [InlineData(new int[] { 4, 2, 1, 7, 8, 1, 2, 8, 1, 0 }, 5, 26)]
        [InlineData(new int[] { 4, 2, 1, 7, 8, 8, 1, 0 }, 3, 23)]
        public void FindMaxSumSubarray_TestCase1(int[] arr, int k, int expectedResult)
        {
            
            var actualResult = _mainService.FindMaxSumSubarray(arr, k);
            Assert.Equal(expectedResult, actualResult);
        }
    }
}
