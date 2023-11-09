/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var rotate = function(nums, k) {
    // let item;
    // for (let i=0; i< k; i++){
    //     item = nums.pop()
    //     nums.unshift(item)// }

    k = k % nums.length; 
    if (k > 0) {
        const rotatedPart = nums.splice(-k);
        nums.unshift(...rotatedPart);
    }
};