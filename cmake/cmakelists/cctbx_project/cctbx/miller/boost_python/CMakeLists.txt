add_python_library ( cctbx_miller_ext
            amplitude_normalisation.cpp
            asu.cpp
            bins.cpp
            change_basis.cpp
            expand_to_p1.cpp
            f_calc_map.cpp
            index_generator.cpp
            index_span.cpp
            lookup_utils.cpp
            match_bijvoet_mates.cpp
            match_indices.cpp
            match_multi_indices.cpp
            merge_equivalents.cpp
            miller_ext.cpp
            phase_integrator.cpp
            phase_transfer.cpp
            randomize_amplitude_and_phase.cpp
            slices.cpp
            sym_equiv.cpp )
target_link_libraries(cctbx_miller_ext cctbx scitbx_boost_python)

