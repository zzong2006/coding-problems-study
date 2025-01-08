/* Given an array of string words, return all strings in words that is a substring of another word. 
You can return the answer in any order.

A substring is a contiguous sequence of characters within a string

Example 1:

Input: words = ["mass","as","hero","superhero"]
Output: ["as","hero"]
Explanation: "as" is substring of "mass" and "hero" is substring of "superhero".
["hero","as"] is also a valid answer.

Example 2:

* Input: words = ["leetcode","et","code"]
* Output: ["et","code"]
* Explanation: "et", "code" are substring of "leetcode".
* Example 3:
* 
* Input: words = ["blue","green","bu"]
* Output: []
* Explanation: No string of words is substring of another string.
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
    vector<string> stringMatching(vector<string>& words) {
        vector<string> result;
        set<string> resultSet;

        for (int i = 0; i < words.size(); i++) {
            for (int j = 0; j < words.size(); j++) {
                if (i != j && (isSubstring(words[i], words[j]))) {
                    resultSet.insert(words[j]);
                }
            }
        }
        return vector<string>(resultSet.begin(), resultSet.end());
    }

    bool isSubstring(string& word, string& subword) {
        return word.find(subword) != string::npos;
    }
};

void testStringMatching() {
    Solution sol;
    
    vector<string> test1 = {"mass","as","hero","superhero"};
    vector<string> expected1 = {"as","hero"};
    vector<string> result1 = sol.stringMatching(test1);
    sort(result1.begin(), result1.end());
    sort(expected1.begin(), expected1.end());
    assert(result1 == expected1);

    vector<string> test2 = {"leetcoder","leetcode","od","hamlet","am"}; 
    vector<string> expected2 = {"leetcode","od", "am"};
    vector<string> result2 = sol.stringMatching(test2);
    sort(result2.begin(), result2.end());
    sort(expected2.begin(), expected2.end());
    if (!(result2 == expected2)) {
        cout << "Test failed. Result: ";
        for (const auto& word : result2) {
            cout << word << " ";
        }
        cout << endl;
    }
    assert(result2 == expected2);

    cout << "All test cases passed!" << endl;
}

int main() {
    testStringMatching();
    return 0;
}

