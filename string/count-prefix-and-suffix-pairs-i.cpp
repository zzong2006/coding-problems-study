/* You are given a 0-indexed string array words.

Let's define a boolean function isPrefixAndSuffix that takes two strings, str1 and str2:

`isPrefixAndSuffix(str1, str2)` returns true if str1 is both a 
prefix
 and a 
suffix
 of str2, and false otherwise.
For example, isPrefixAndSuffix("aba", "ababa") is true because "aba" is a prefix of "ababa" and also a suffix, but isPrefixAndSuffix("abc", "abcd") is false.

Return an integer denoting the number of index pairs (i, j) such that i < j, and isPrefixAndSuffix(words[i], words[j]) is true.

 

Example 1:

Input: words = ["a","aba","ababa","aa"]
Output: 4
Explanation: In this example, the counted index pairs are:
i = 0 and j = 1 because isPrefixAndSuffix("a", "aba") is true.
i = 0 and j = 2 because isPrefixAndSuffix("a", "ababa") is true.
i = 0 and j = 3 because isPrefixAndSuffix("a", "aa") is true.
i = 1 and j = 2 because isPrefixAndSuffix("aba", "ababa") is true.
Therefore, the answer is 4.

*/

#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <cassert>

using namespace std;

class Solution {
public:
    int countPrefixSuffixPairs(vector<string>& words) {
        int count = 0;
        for (int i = 0; i < words.size(); i++) {
            for (int j = 0; j < words.size(); j++) {
                if (i < j && isPrefixAndSuffix(words[i], words[j])) {
                    cout << words[i] << " " << words[j] << endl;
                    count++;
                }
            }
        }
        return count;
    }

    bool isPrefixAndSuffix(string& str1, string& str2) {
        if (str1.size() > str2.size()) {
            return false;
        }

        for (int i = 0; i < str1.size(); i++) {
            if (str1[i] != str2[i]) {
                return false;
            }
        }
        for (int i = 0; i < str1.size(); i++) {
            if (str2[str2.size() - str1.size() + i] != str1[i]) {
                return false;
            }
        }
        return true;
    }
};

void testStringMatching() {
    Solution sol;
    
    vector<string> test1 = {"a","aba","ababa","aa"};
    int expected1 = 4;
    int result1 = sol.countPrefixSuffixPairs(test1);
    if (expected1 != result1) {
        cout << "Test failed. Result: " << result1 << endl;
    }
    assert(result1 == expected1);

    vector<string> test2 = {"abab", "ab"};
    int expected2 = 0;
    int result2 = sol.countPrefixSuffixPairs(test2);
    if (expected2 != result2) {
        cout << "Test failed. Result: " << result2 << endl;
    }
    assert(result2 == expected2);

    vector<string> test4 = {"bb", "bb"};
    int expected4 = 1;
    int result4 = sol.countPrefixSuffixPairs(test4);
    if (expected4 != result4) {
        cout << "Test failed. Result: " << result4 << endl;
    }
    assert(result4 == expected4);

    vector<string> test3 = {"a", "abb"};
    int expected3 = 0;
    int result3 = sol.countPrefixSuffixPairs(test3);
    if (expected3 != result3) {
        cout << "Test failed. Result: " << result3 << endl;
    }
    assert(result3 == expected3);

    cout << "All test cases passed!" << endl;
}

int main() {
    testStringMatching();
    return 0;
}

