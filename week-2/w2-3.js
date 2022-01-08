function maxProduct(nums){
    let a = nums.length
    let max = 0
    for(let x = 0; x<a; x++){
        for(let y = x+1; y<a; y++){
            let maxf = nums[x]*nums[y];
            if(max == 0){
                max = maxf;
            }
            if(maxf > max){
                max=maxf;
            }
        }
    }
    console.log(max); 
}
maxProduct([5, 20, 2, 6]) // 得到 120
maxProduct([10, -20, 0, 3]) // 得到 30
maxProduct([-1, 2]) // 得到 -2
maxProduct([-1, 0, 2]) // 得到 0
maxProduct([-1, -2, 0]) // 得到 2
