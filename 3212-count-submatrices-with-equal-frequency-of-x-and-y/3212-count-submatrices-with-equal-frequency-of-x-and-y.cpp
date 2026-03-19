class Solution {
public:
    int numberOfSubmatrices(vector<vector<char>>& grid) {
        // we deine the matrix and the size of it 
        int m = grid.size(), n = grid[0].size();
        // vextors X, Y with size n, initailized to 0
        vector<int> colX(n, 0), colY(n, 0);
        int ans = 0;
        // we loop throught the matrix 
        for (int i =0; i < m; i++){
            for (int j =0; j<n; j++){
                // if we find the elements of interest, increament the counters for the respective elements of interest in a one array counter. 
                if (grid[i][j] == 'X') colX[j]++;
                else if (grid[i][j] == 'Y') colY[j]++;
            }
            // initialize the prefix counters
            int prefX = 0, prefY = 0;
            for (int j =0; j < n; j++){
                // loop through the evtro and prefix sum the elements 
                prefX += colX[j];
                prefY += colY[j];
            // if the conditions of interest is met, then retun the answer of interest.
                if (prefX == prefY && prefX > 0 ){
                    ans++;
                }
            }
        }
        return ans;



        
    }
};