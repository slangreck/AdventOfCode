import sys
import re

def main():
    file = sys.stdin
    if file.isatty():
        filename = input('Input file name: ')
        file = open(filename)
    
    rules = file.readlines()
    file.close()

    bags = parseRules(rules)

    shinyGoldBag = bags['shiny gold']
    shinyGoldContainers = shinyGoldBag.findContainers()
    print(f'Shiny gold bags can be carried in {len(shinyGoldContainers)} other bags')
    print(f'Shiny gold bags must contain {shinyGoldBag.countContainedBags()} other bags')

def parseRules(rules):
    bags = {bag.color: bag for bag in [Bag(rule) for rule in rules]}

    ruleRegex = re.compile(r'(\d+) ([a-z]+ [a-z]+) bags?')
    for bag in bags.values():
        for rule in bag.containsRule.split(', '):
            match = ruleRegex.match(rule)
            if match and match.group(2) in bags:
                cBag = bags[match.group(2)]
                bag.contains[cBag.color] = ContainedBag(cBag, int(match.group(1)))
                cBag.containedIn[bag.color] = bag

    return bags


class Bag:
    def __init__(self, rule):
        (color, restOfRule) = rule.split(' bags contain ')
        self.color = color
        self.containsRule = restOfRule.strip('. \r\n')
        self.contains = {}
        self.containedIn = {}

    def findContainers(self, containers = set()):
        for container in self.containedIn.values():
            if container not in containers:
                containers.add(container)
                container.findContainers(containers)

        return containers

    def countContainedBags(self):
        count = 0
        for contained in self.contains.values():
            count += contained.count + contained.count * contained.bag.countContainedBags()

        return count

class ContainedBag:
    def __init__(self, bag, count):
        self.bag = bag
        self.count = count

if __name__ == "__main__":
    main()