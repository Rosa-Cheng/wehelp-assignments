function maxZeros(nums){
    let counter = 0
    let result = 0
    for(let i=0; i<nums.length; i++){
        if(nums[i] == 0){
            counter += 1;
            if(counter>result){
                result = counter;
            }
        }
        else{
        counter = 0;
        }
    }
    console.log(result);
    }
    maxZeros([0, 1, 0, 0]); // 得到 2
    maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]); // 得到 4
    maxZeros([1, 1, 1, 1, 1]); // 得到 0
    maxZeros([0, 0, 0, 1, 1]) // 得到 3