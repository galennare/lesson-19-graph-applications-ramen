import matplotviz as viz
import buildings_setup as bs
import kruskals

if __name__ == '__main__':
    mst = kruskals.kruskals_algorithm(bs.g)
    bs.pp.pprint(mst)
