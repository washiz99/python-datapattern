from src.datapattern import DataPattern


class TestDataPattern():

    def test_example(self):
        expected = 3
        assert expected == 1 + 2

    def test_product(self):
        factor = [
            [
                ['coffee', 'coke'],
                ['L', 'M', 'S'],
            ]
        ]
        pattern = DataPattern(factor)
        result = pattern._product(*[
                ['coffee', 'coke'],
                ['L', 'M', 'S'],
            ]
        )

        expected = [
            ['coffee', 'L'],
            ['coffee', 'M'],
            ['coffee', 'S'],
            ['coke', 'L'],
            ['coke', 'M'],
            ['coke', 'S'],
        ]
        assert expected == result

    def test_multiple_array_size(self):

        factor = [
            [
                # 2 * 3
                ['coffee', 'coke'],
                ['L', 'M', 'S'],
            ]
        ]
        pattern = DataPattern(factor)
        result = pattern.get_pattern_size()
        assert 6 == result

    def test_generate(self):
        # drink and size pattern
        factor = [
            [
                ['coffee', 'coke'],
                ['L', 'M', 'S'],
            ]
        ]
        pattern = DataPattern(factor)
        result = pattern.generate()

        expected = [
            [
                ['coffee', 'L'],
                ['coffee', 'M'],
                ['coffee', 'S'],
                ['coke', 'L'],
                ['coke', 'M'],
                ['coke', 'S'],
            ]
        ]
        assert expected == result

    def test_generate_2d(self):

        factor = [
            # place and cost pattern
            [
                ['tokyo', 'osaka'],
                ['high', 'row'],
            ],
            # drink pattern
            [
                ['coffee', 'coke'],
            ]
        ]
        pattern = DataPattern(factor)
        result = pattern.generate()

        expected = [
            [
                ['tokyo', 'high'],
                ['tokyo', 'high'],
                ['tokyo', 'row'],
                ['tokyo', 'row'],
                ['osaka', 'high'],
                ['osaka', 'high'],
                ['osaka', 'row'],
                ['osaka', 'row'],
            ],
            [
                ['coffee'],
                ['coke'],
                ['coffee'],
                ['coke'],
                ['coffee'],
                ['coke'],
                ['coffee'],
                ['coke'],
            ]
        ]
        assert expected == result

    def test_generate_3d(self):

        factor = [
            # place and cost pattern
            [
                ['tokyo', 'osaka'],
                ['high', 'row'],
            ],
            # drink pattern
            [
                ['coffee', 'coke'],
            ],
            # price pattern
            [
                [100, 200],
            ]
        ]
        pattern = DataPattern(factor)
        result = pattern.generate()

        expected = [
            [
                ['tokyo', 'high'],
                ['tokyo', 'high'],
                ['tokyo', 'high'],
                ['tokyo', 'high'],
                ['tokyo', 'row'],
                ['tokyo', 'row'],
                ['tokyo', 'row'],
                ['tokyo', 'row'],
                ['osaka', 'high'],
                ['osaka', 'high'],
                ['osaka', 'high'],
                ['osaka', 'high'],
                ['osaka', 'row'],
                ['osaka', 'row'],
                ['osaka', 'row'],
                ['osaka', 'row'],
            ],
            [
                ['coffee'],
                ['coffee'],
                ['coke'],
                ['coke'],
                ['coffee'],
                ['coffee'],
                ['coke'],
                ['coke'],
                ['coffee'],
                ['coffee'],
                ['coke'],
                ['coke'],
                ['coffee'],
                ['coffee'],
                ['coke'],
                ['coke'],
            ],
            [
                [100],
                [200],
                [100],
                [200],
                [100],
                [200],
                [100],
                [200],
                [100],
                [200],
                [100],
                [200],
                [100],
                [200],
                [100],
                [200],
            ]
        ]
        assert expected == result
