public class RandomizedSet {
    HashSet<int> randomSet;
    List<int> elements;
    Random random = new Random();

    public RandomizedSet() {
        randomSet = new HashSet<int>();
        elements = new List<int>();
    }
    
    public bool Insert(int val) {
        if(randomSet.Contains(val)){
            return false;
        }
        else{
            randomSet.Add(val);
            elements.Add(val);
            return true;
        }
    }
    
    public bool Remove(int val) {
        if(randomSet.Contains(val)){
            randomSet.Remove(val);

            int valIndex = elements.IndexOf(val);
            int lastElement = elements[elements.Count - 1];
            elements[valIndex] = lastElement;
            elements.RemoveAt(elements.Count - 1);

            return true;
        }
        else{
            return false;
        }
    }
    
    public int GetRandom() {
        int randomIndex = random.Next(elements.Count); // Generate a random index
        return elements[randomIndex];
    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet obj = new RandomizedSet();
 * bool param_1 = obj.Insert(val);
 * bool param_2 = obj.Remove(val);
 * int param_3 = obj.GetRandom();
 */
