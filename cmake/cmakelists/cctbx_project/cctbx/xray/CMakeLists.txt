add_python_library ( cctbx_xray_ext
            boost_python/conversions.cpp
            boost_python/curvatures_simple.cpp
            boost_python/extinction.cpp
            boost_python/f_model_bpl.cpp
            boost_python/fast_gradients.cpp
            boost_python/gradient_flags.cpp
            boost_python/gradients_direct.cpp
            boost_python/grouped_data.cpp
            boost_python/minimization.cpp
            boost_python/parameter_map.cpp
            boost_python/sampled_model_density.cpp
            boost_python/sampling_base.cpp
            boost_python/scatterer.cpp
            boost_python/scatterer_flags.cpp
            boost_python/scattering_type_registry.cpp
            boost_python/structure_factors_direct.cpp
            boost_python/structure_factors_simple.cpp
            boost_python/targets.cpp
            boost_python/twin_components.cpp
            boost_python/twin_targets.cpp
            boost_python/xray_ext.cpp
            targets/shelxl_wght_ls_bpl.cpp )
target_link_libraries(cctbx_xray_ext cctbx scitbx_boost_python omptbx fable)

add_subdirectory(observations)
