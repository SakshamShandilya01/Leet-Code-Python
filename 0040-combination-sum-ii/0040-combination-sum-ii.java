class Solution {
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        Arrays.sort(candidates);
        List<List<Integer>> result=new ArrayList<>();
        combinations(0,candidates,target,new ArrayList<>(),result);
        return result;
            }
    public void combinations(int index, int[] candidates, int target, List<Integer> ans,List<List<Integer>> result){
                if(target==0){
                    result.add(new ArrayList<>(ans));
                    return;
                }
                 for(int i=index;i<candidates.length;i++){
                    if(i>index && candidates[i]==candidates[i-1]){
                        continue;
                    }
                    if(candidates[i]>target){
                        break;
                    }
                    ans.add(candidates[i]);
                    combinations(i+1, candidates, target-candidates[i], ans, result);
                    ans.remove(ans.size()-1);
                 }
            }
}