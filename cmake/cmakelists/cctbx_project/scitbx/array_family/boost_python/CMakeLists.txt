add_python_library ( scitbx_array_family_flex_ext
            flex_ext.cpp
            flex_grid.cpp
            flex_bool.cpp
            flex_size_t.cpp
            flex_int.cpp
            flex_long.cpp
            flex_float.cpp
            flex_double.cpp
            flex_double_matrix.cpp
            flex_complex_double.cpp
            flex_std_string.cpp
            flex_random.cpp
            flex_sort.cpp
            flex_histogram.cpp
            flex_weighted_histogram.cpp
            flex_mean_and_variance.cpp
            flex_median.cpp
            flex_linear_interpolation.cpp
            flex_vec3_double.cpp
            flex_vec2_double.cpp
            flex_vec3_int.cpp
            flex_sym_mat3_double.cpp
            flex_mat3_double.cpp
            flex_tiny_size_t_2.cpp
            loops.cpp
            show_sizes.cpp
            numpy_bridge.cpp )
target_link_libraries(scitbx_array_family_flex_ext scitbx_boost_python)

add_python_library ( scitbx_array_family_shared_ext
            shared_ext.cpp )
target_link_libraries(scitbx_array_family_shared_ext scitbx_boost_python)

add_python_library ( regression_test_ext
            regression_test_ext.cpp )
target_link_libraries(regression_test_ext scitbx_boost_python)

