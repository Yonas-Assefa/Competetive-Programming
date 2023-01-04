class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:

        ans = []
        dic = {}

        for cpdomain in cpdomains:
            count_paired_domain = cpdomain.split(" ")
            no_user = int(count_paired_domain[0])
            domain = count_paired_domain[1].split(".")
            no_subdomain = len(domain)

            for i in range(no_subdomain - 1, -1, -1):
                subdomain = ".".join(domain[i:])
                dic[subdomain] = dic.get(subdomain, 0) + no_user
        
        for subdomain in dic:
            count_paired_subdomian = str(dic[subdomain]) + " "  +  subdomain
            ans.append(count_paired_subdomian)
        return ans
  