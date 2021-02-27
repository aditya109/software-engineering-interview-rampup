using System;
using System.Collections.Generic;
using System.Linq;

namespace Main.Service
{
    public class MainService
    {
        /** 
         * In a row of trees, the i-th tree produces fruit with type tree[i].
         * You start at any tree of your choice, then repeatedly perform the following steps:
         * 
         * Add one piece of fruit from this tree to your baskets.If you cannot, stop.
         * Move to the next tree to the right of the current tree.  If there is no tree to the right, stop.
         * Note that you do not have any choice after the initial choice of starting tree: you must perform step 1, then step 2, then back to step 1, then step 2, and so on until you stop.
         * You have two baskets, and each basket can carry any quantity of fruit, but you want each basket to only carry one type of fruit each.
         * What is the total amount of fruit you can collect with this procedure?
         * 
         * Example Input: [3,3,3,1,2,1,1,2,3,3,4]
         * Output: 5
         * Explanation: We can collect [1,2,1,1,2].
         * If we started at the first tree or the eighth tree, we would only collect 4 fruits.
         */
        public int Run(int[] tree, int basketCount)
        {
            int windowStart = 0;
            int totalFruitCount = int.MinValue;
            int currentFruitsInBasket = 0;
            Dictionary<int, int> fruitTypeFrequency =
                new Dictionary<int, int>();

            for (int windowEnd = 0; windowEnd < tree.Length; windowEnd++)
            {
                currentFruitsInBasket++;

                if (fruitTypeFrequency.ContainsKey(tree[windowEnd]))
                {
                    fruitTypeFrequency[tree[windowEnd]] += 1;
                }
                else
                {
                    fruitTypeFrequency[tree[windowEnd]] = 1;
                }
                List<int> keys = new List<int>(fruitTypeFrequency.Keys);
                if (keys.Count() > basketCount)
                {
                    totalFruitCount =
                        Math.Max(totalFruitCount, currentFruitsInBasket - 1);
                    fruitTypeFrequency[tree[windowStart]] -= 1;
                    if (fruitTypeFrequency[tree[windowStart]] == 0)
                    {
                        fruitTypeFrequency.Remove(tree[windowStart]);
                    }
                    currentFruitsInBasket--;
                    windowStart++;
                }
            }
            return new List<int>(fruitTypeFrequency.Values).Sum();
        }
    }
}
