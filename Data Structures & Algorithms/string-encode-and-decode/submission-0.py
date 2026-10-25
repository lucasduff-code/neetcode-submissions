class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(word)}#{word}" for word in strs)

    def decode(self, s: str) -> List[str]:
        decoded_list = []
        i = 0

        while i < len(s):
            j = s.index("#", i)
            word_len = int(s[i:j])

            start = j + 1
            end = start + word_len
            decoded_list.append(s[start:end])

            i = end

        return decoded_list

