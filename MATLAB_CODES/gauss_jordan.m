function X = gauss_jordan(A, B)
    % Gauss-Jordan Method for solving AX = B
    % A -> Coefficient matrix (n x n)
    % B -> Constant matrix (n x 1)
    % X -> Solution vector (n x 1)

    % Augment matrix A with B
    Aug = [A B];  
    [n, m] = size(Aug);

    % Forward elimination
    for i = 1:n
        % Pivot: Making the diagonal element 1
        Aug(i, :) = Aug(i, :) / Aug(i, i); 

        % Making other elements in column zero
        for j = 1:n
            if i ~= j
                Aug(j, :) = Aug(j, :) - Aug(j, i) * Aug(i, :);
            end
        end
    end

    % Extracting solution
    X = Aug(:, end);
end

% Example usage:
A = [2 -1 3; 4 2 -2; 1 1 1];
B = [5; 3; 4];
X = gauss_jordan(A, B);
disp('Solution:');
disp(X);
