add_executable(tst_collision_detection tst_collision_detection.cc)
add_test(NAME tst_collision_detection COMMAND tst_collision_detection)

add_executable(tst_octree tst_octree.cc)
add_test(NAME tst_octree COMMAND tst_octree)

add_executable(tst_quadtree tst_quadtree.cc)
add_test(NAME tst_quadtree COMMAND tst_quadtree)

