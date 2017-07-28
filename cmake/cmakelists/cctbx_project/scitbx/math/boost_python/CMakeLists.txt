add_python_library ( scitbx_math_ext
            math_ext.cpp
            basic_statistics.cpp
            gaussian.cpp
            golay.cpp
            minimum_covering_sphere.cpp
            principal_axes_of_inertia.cpp
            row_echelon.cpp
            tensor_rank_2.cpp
            chebyshev.cpp
            icosahedron.cpp
            slatec.cpp
            line_search.cpp
            r3_rotation.cpp
            resample.cpp
            quadrature.cpp
            unimodular_generator.cpp
            halton.cpp
            least_squares_plane.cpp
            continued_fraction.cpp
            numeric_limits.cpp
            distributions.cpp
            exp_functions.cpp
            zernike.cpp
            zernike_moments.cpp
            2d_zernike_moments.cpp
            weighted_covariance.cpp
            rotation.cpp
            interpolation.cpp
            tetrahedron.cpp
            angle_derivative.cpp )
target_link_libraries(scitbx_math_ext scitbx_slatec scitbx_boost_python)

