function sumPairs (array,desiredNum) {
    let pairs = []
    let currentNum
    while (array.length > 0) {
        currentNum = array.shift()
        for (let n of array) {
            if (currentNum + n === desiredNum) {
                pairs.push([currentNum, n])
            }
        }
    }
    return pairs.length > 0 ? pairs : 'unable to find pairs'
};