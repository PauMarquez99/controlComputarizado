h1 = tf([0 0 3],[1 0.5 0], 'iodelay', 2);
hd1 = c2d(h1, 2);

h2 = tf([1 0.3 0],[1 0.5 -0.14]);
hd2 = c2d(h2, 0.1);
