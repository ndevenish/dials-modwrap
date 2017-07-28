add_python_library ( dials_algorithms_spatial_indexing_ext
            octree.cc
            quadtree.cc
            spatial_indexing_ext.cc )
target_link_libraries(dials_algorithms_spatial_indexing_ext cctbx scitbx_boost_python)

