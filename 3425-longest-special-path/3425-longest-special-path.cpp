#include <vector>
#include <algorithm>
#include <functional>
using namespace std;

class Solution {
public:
    vector<int> longestSpecialPath(vector<vector<int>>& e, vector<int>& n) {
        int sz = n.size();
        vector<vector<pair<int, int>>> g(sz);
        for (auto& edge : e) {
            g[edge[0]].emplace_back(edge[1], edge[2]);
            g[edge[1]].emplace_back(edge[0], edge[2]);
        }

        int maxVal = *max_element(n.begin(), n.end());
        vector<int> last(maxVal + 1, -1);

        vector<pair<int, long long>> st;
        int s = 0, maxL = 0, minN = 1;

        function<void(int, int, long long)> dfs = [&](int v, int p, long long d) {
            int idx = st.size();
            int oldPos = last[n[v]];
            int oldS = s;
            if (oldPos != -1 && oldPos >= s) {
                s = oldPos + 1;
            }

            st.emplace_back(v, d);
            last[n[v]] = idx;

            if (idx >= s) {
                long long len = d;
                if (s > 0) {
                    len -= st[s].second;
                }

                int nodes = idx - s + 1;
                if (len > maxL) {
                    maxL = len;
                    minN = nodes;
                } else if (len == maxL) {
                    if (nodes < minN) {
                        minN = nodes;
                    }
                }
            }

            for (auto& [neigh, w] : g[v]) {
                if (neigh == p) continue;
                dfs(neigh, v, d + w);
            }

            last[n[v]] = oldPos;
            st.pop_back();
            s = oldS;
        };

        dfs(0, -1, 0);
        return {maxL, minN};
    }
};