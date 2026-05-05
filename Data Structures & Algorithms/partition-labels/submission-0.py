class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ch_last_index_map = {}
        for i, ch in enumerate(s):
            ch_last_index_map[ch] = i
        
        answer = []
        partition_size = 0
        end_pointer = 0

        for i, ch in enumerate(s):
            partition_size += 1

            end_pointer = max(end_pointer, ch_last_index_map[ch])

            if i == end_pointer:
                answer.append(partition_size)
                partition_size = 0

        return answer