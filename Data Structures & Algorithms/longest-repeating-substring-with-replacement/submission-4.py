class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ch_to_freq = defaultdict(int)
        ans = 0
        l = 0

        for r in range(len(s)):
            ch_to_freq[s[r]] += 1
            while (r - l + 1) - max(ch_to_freq.values()) > k:
                ch_to_freq[s[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)
        return ans

