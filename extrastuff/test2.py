import time
import pdftofasta


fileN = raw_input("Enter PDB file path: ")
print "Processing data for " + fileN + "\nPlease Wait..."
time.sleep(1)

if __name__ == '__main__':
    
    import argparse


    parser = argparse.ArgumentParser(
        description='Converts amino acid residues from PDB file into a FASTA string',

        formatter_class=argparse.RawTextHelpFormatter
        )


    parser.add_argument('PDBfile')

    parser.add_argument('-l', '--ligand', action='store_true', help='includes HETATM residues.')
    parser.add_argument('-o', '--out', metavar='out.fasta', type=str, 
            help='writes FASTA strings to an output file instead of printing it to the screen')
    parser.add_argument('-v', '--version', action='version', version='pdb_to_fasta v. 1.0')



    args = parser.parse_args()
    
    in_pdb = Pdb(args.PDBfile)

    fastas = sorted(in_pdb.to_fasta(hetatm=args.ligand).items())
    
    if args.out:
        with open(args.out, 'w') as out:
            for chain in fastas:
                out.write('>Chain {}:\n'.format(chain[0]))
                for amino_code in chain[1]:
                    out.write(amino_code)
                out.write('\n\n')
                
    else:
        for chain in fastas:
            print('>Chain {}:\n'.format(chain[0]))
            amino_list = []
            for amino_code in chain[1]:
                amino_list.append(amino_code)
            print("".join(amino_list))
            print('\n\n')       
