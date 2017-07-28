add_python_library ( cctbx_maptbx_ext
            basic_map.cpp
            coordinate_transformers.cpp
            grid_indices_around_sites.cpp
            grid_tags.cpp
            gridding.cpp
            mapper.cpp
            maptbx_ext.cpp
            misc.cpp
            peak_search.cpp
            pymol_interface.cpp
            real_space_refinement.cpp
            statistics.cpp
            structure_factors.cpp )
target_link_libraries(cctbx_maptbx_ext cctbx omptbx scitbx_boost_python)

