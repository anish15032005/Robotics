% Define vertices of a tesseract
vertices = [
    0 0 0 0;
    0 0 0 1;
    0 0 1 0;
    0 0 1 1;
    0 1 0 0;
    0 1 0 1;
    0 1 1 0;
    0 1 1 1;
    1 0 0 0;
    1 0 0 1;
    1 0 1 0;
    1 0 1 1;
    1 1 0 0;
    1 1 0 1;
    1 1 1 0;
    1 1 1 1
];

% Projection to 3D
projection_matrix = [1 0 0 0; 
                     0 1 0 0; 
                     0 0 1 0];
vertices_3d = vertices * projection_matrix';

% Define edges of a tesseract
edges = [
    1 2; 1 3; 1 5; 2 4; 2 6; 3 4; 3 7;
    4 8; 5 6; 5 7; 6 8; 7 8;
    9 10; 9 11; 9 13; 10 12; 10 14; 11 12;
    11 15; 12 16; 13 14; 13 15; 14 16; 15 16;
    1 9; 2 10; 3 11; 4 12; 5 13; 6 14;
    7 15; 8 16
];

% Plotting the tesseract
figure;
hold on;
for i = 1:size(edges, 1)
    x = [vertices_3d(edges(i, 1), 1), vertices_3d(edges(i, 2), 1)];
    y = [vertices_3d(edges(i, 1), 2), vertices_3d(edges(i, 2), 2)];
    z = [vertices_3d(edges(i, 1), 3), vertices_3d(edges(i, 2), 3)];
    plot3(x, y, z, 'b');
end

% Set plot limits and labels
axis equal;
xlabel('X');
ylabel('Y');
zlabel('Z');
title('3D Projection of a Tesseract');
grid on;
hold off;