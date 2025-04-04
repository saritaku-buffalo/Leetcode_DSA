class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_email = set()
        for i in emails:
            j, local = 0, ""
            while i[j] not in ["@", "+"]:
                if i[j] != ".":
                    local += i[j]
                j += 1
            while i[j]  != "@": 
                j += 1
            domain = i[j+1:]
            unique_email.add((local,domain))
        return(len(unique_email))


# Another solution
class Solution:
    def numUniqueEmails(self, emails):
        unique_email = set()
        for i in emails:
            local, domain = i.split('@')
            local = local.replace('.', "")
            local = local.split('+')[0]
            unique_email.add(local,domain)
        return(len(unique_email))