from inference import main


class DiffDockInferenceClient:

    def __init__(
        self,
        config: str = 'default_inference_args.yaml',
        protein_ligand_csv: str = None,
        complex_name: str = None,
        protein_path: str = None,
        protein_sequence: str = None,
        ligand_description: str = 'CCCCC(NC(=O)CCC(=O)O)P(=O)(O)OC1=CC=CC=C1',
        out_dir: str = 'results/user_inference',
        save_visualisation: bool = False,
        samples_per_complex: int = 10,
        model_dir: str = None,
        ckpt: str = 'best_ema_inference_epoch_model.pt',
        confidence_model_dir: str = None,
        confidence_ckpt: str = 'best_model.pt',
        batch_size: int = 10,
        no_final_step_noise: bool = True,
        inference_steps: int = 10,
        actual_steps: int = None,
        old_score_model: bool = False,
        old_confidence_model: bool = True,
        initial_noise_std_proportion: float = -1.0,
        choose_residue: bool = False,
        temp_sampling_tr: float = 1.0,
        temp_psi_tr: float = 0.0,
        temp_sigma_data_tr: float = 0.5,
        temp_sampling_rot: float = 1.0,
        temp_psi_rot: float = 0.0,
        temp_sigma_data_rot: float = 0.5,
        temp_sampling_tor: float = 1.0,
        temp_psi_tor: float = 0.0,
        temp_sigma_data_tor: float = 0.5,
        gnina_minimize: bool = False,
        gnina_path: str = 'gnina',
        gnina_log_file: str = 'gnina_log.txt',
        gnina_full_dock: bool = False,
        gnina_autobox_add: float = 4.0,
        gnina_poses_to_optimize: int = 1,
    ) -> None:
        """
        :param config:
        :param protein_ligand_csv: Path to a .csv file specifying the input as described in the README. If this is not None, it will be used instead of the protein_path, protein_sequence and ligand parameters
        :param complex_name: Name that the complex will be saved with
        :param protein_path: Path to the protein file
        :param protein_sequence: Sequence of the protein for ESMFold, this is ignored if protein_path is not None
        :param ligand_description: Either a SMILES string or the path to a molecule file that rdkit can read
        :param out_dir: Directory where the outputs will be written to
        :param save_visualisation: Save a pdb file with all of the steps of the reverse diffusion
        :param samples_per_complex: Number of samples to generate
        :param model_dir: Path to folder with trained score model and hyperparameters
        :param ckpt: Checkpoint to use for the score model
        :param confidence_model_dir: Path to folder with trained confidence model and hyperparameters
        :param confidence_ckpt: Checkpoint to use for the confidence model
        :param batch_size:
        :param no_final_step_noise: Use no noise in the final step of the reverse diffusion
        :param inference_steps: Number of denoising steps
        :param actual_steps: Number of denoising steps that are actually performed
        :param old_score_model:
        :param old_confidence_model:
        :param initial_noise_std_proportion: Initial noise std proportion
        :param choose_residue:
        :param temp_sampling_tr:
        :param temp_psi_tr:
        :param temp_sigma_data_tr:
        :param temp_sampling_rot:
        :param temp_psi_rot:
        :param temp_sigma_data_rot:
        :param temp_sampling_tor:
        :param temp_psi_tor:
        :param temp_sigma_data_tor:
        :param gnina_minimize:
        :param gnina_path:
        :param gnina_log_file: To redirect gnina subprocesses stdouts from the terminal window
        :param gnina_full_dock:
        :param gnina_autobox_add:
        :param gnina_poses_to_optimize:
        """
        self.config = config
        self.protein_ligand_csv = protein_ligand_csv
        self.complex_name = complex_name
        self.protein_path = protein_path
        self.protein_sequence = protein_sequence
        self.ligand_description = ligand_description
        self.out_dir = out_dir
        self.save_visualisation = save_visualisation
        self.samples_per_complex = samples_per_complex
        self.model_dir = model_dir
        self.ckpt = ckpt
        self.confidence_model_dir = confidence_model_dir
        self.confidence_ckpt = confidence_ckpt
        self.batch_size = batch_size
        self.no_final_step_noise = no_final_step_noise
        self.inference_steps = inference_steps
        self.actual_steps = actual_steps
        self.old_score_model = old_score_model
        self.old_confidence_model = old_confidence_model
        self.initial_noise_std_proportion = initial_noise_std_proportion
        self.choose_residue = choose_residue
        self.temp_sampling_tr = temp_sampling_tr
        self.temp_psi_tr = temp_psi_tr
        self.temp_sigma_data_tr = temp_sigma_data_tr
        self.temp_sampling_rot = temp_sampling_rot
        self.temp_psi_rot = temp_psi_rot
        self.temp_sigma_data_rot = temp_sigma_data_rot
        self.temp_sampling_tor = temp_sampling_tor
        self.temp_psi_tor = temp_psi_tor
        self.temp_sigma_data_tor = temp_sigma_data_tor
        self.gnina_minimize = gnina_minimize
        self.gnina_path = gnina_path
        self.gnina_log_file = gnina_log_file
        self.gnina_full_dock = gnina_full_dock
        self.gnina_autobox_add = gnina_autobox_add
        self.gnina_poses_to_optimize = gnina_poses_to_optimize

    def execute(self) -> None:
        main(self)