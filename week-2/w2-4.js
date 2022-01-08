function twoSum(nums, target){
    for(let x=0; x<nums.length;x++){
        let goal=target-nums[x];
        for(let y=x+1; y<nums.length; y++){
            if(nums[y]===goal)
            return [x,y];
        }
    }
}
    let result=twoSum([2, 11, 7, 15], 9);
    console.log(result);// show [0, 2] because nums[0]+nums[2] is 9