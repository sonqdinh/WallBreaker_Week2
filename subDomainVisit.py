from collections import defaultdict

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        count = defaultdict(int)
        
        for domainVisit in cpdomains:
            nVisit, domains = domainVisit.split(" ")
            nVisit = int(nVisit)
            domains = domains.split('.')[::-1]
            
            domain = ''
            for i in range(len(domains)):
                domain = domains[i] + domain
                count[domain] += nVisit
                domain = '.' + domain
        
        ans = []
        for domain in count:
            ans.append(str(count[domain]) + ' ' + domain)
        
        return ans