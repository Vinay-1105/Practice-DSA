class MyHashSet(object):

    def __init__(self):
        # Ek fixed size array banate hain kyunki key 0 se 10^6 ke beech hi hoga
        # Har index par False rakhenge, matlab vo key abhi set mein nahi hai
        self.data = [False] * 1000001

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        # Key ko add karne ke liye uske index par True set kar do
        # Matlab vo key ab HashSet mein aa gaya hai
        self.data[key] = True

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        # Key ko remove karne ke liye uske index par False set kar do
        # Matlab vo key ab HashSet se remove ho gaya hai
        self.data[key] = False

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        # Check karo ki data[key] True hai ya nahi
        # True ka matlab key set mein present hai, False matlab missing hai
        return self.data[key]