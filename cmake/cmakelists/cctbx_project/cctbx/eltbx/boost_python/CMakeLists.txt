add_python_library ( cctbx_eltbx_attenuation_coefficient_ext
            attenuation_coefficient_ext.cpp )
target_link_libraries(cctbx_eltbx_attenuation_coefficient_ext cctbx scitbx_boost_python)

add_python_library ( cctbx_eltbx_chemical_elements_ext
            chemical_elements_ext.cpp )
target_link_libraries(cctbx_eltbx_chemical_elements_ext cctbx scitbx_boost_python)

add_python_library ( cctbx_eltbx_covalent_radii_ext
            covalent_radii_ext.cpp )
target_link_libraries(cctbx_eltbx_covalent_radii_ext cctbx scitbx_boost_python)

add_python_library ( cctbx_eltbx_fp_fdp_ext
            fp_fdp_ext.cpp )
target_link_libraries(cctbx_eltbx_fp_fdp_ext cctbx scitbx_boost_python)

add_python_library ( cctbx_eltbx_henke_ext
            henke_ext.cpp )
target_link_libraries(cctbx_eltbx_henke_ext cctbx scitbx_boost_python)

add_python_library ( cctbx_eltbx_icsd_radii_ext
            icsd_radii_ext.cpp )
target_link_libraries(cctbx_eltbx_icsd_radii_ext cctbx scitbx_boost_python)

add_python_library ( cctbx_eltbx_neutron_ext
            neutron_ext.cpp )
target_link_libraries(cctbx_eltbx_neutron_ext cctbx scitbx_boost_python)

add_python_library ( cctbx_eltbx_sasaki_ext
            sasaki_ext.cpp )
target_link_libraries(cctbx_eltbx_sasaki_ext cctbx scitbx_boost_python)

add_python_library ( cctbx_eltbx_tiny_pse_ext
            tiny_pse_ext.cpp )
target_link_libraries(cctbx_eltbx_tiny_pse_ext cctbx scitbx_boost_python)

add_python_library ( cctbx_eltbx_wavelengths_ext
            wavelengths_ext.cpp )
target_link_libraries(cctbx_eltbx_wavelengths_ext cctbx scitbx_boost_python)

add_python_library ( cctbx_eltbx_xray_scattering_ext
            xray_scattering_ext.cpp )
target_link_libraries(cctbx_eltbx_xray_scattering_ext cctbx scitbx_boost_python)

